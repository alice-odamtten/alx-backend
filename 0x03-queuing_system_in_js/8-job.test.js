import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ redis: { createClientFactory: () => kue.redis.createClient({ host: '127.0.0.1', port: 6379, auth_pass: 'yourpassword' }) }, jobEvents: false });
    kue.TestMode.clearQueue(queue);
  });

  afterEach(() => {
    kue.TestMode.clearQueue(queue);
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].log[0]).to.contain('Notification job created:');
    expect(queue.testMode.jobs[1].log[0]).to.contain('Notification job created:');
  });
});
