import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklistedNumbers.includes(phoneNumber)) {
    job.failed(new Error(`Phone number ${phoneNumber} is blacklisted`));
    done();
  } else {
    job.progress(50, 100);

    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    setTimeout(() => {
       done();
    }, 1000);
  }
}

const queue = kue.createQueue({ concurrency: 2, jobEvents: false });

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

process.on('SIGINT', () => {
  queue.shutdown(5000, (err) => {
    console.log('Kue shutdown:', err || '');
    process.exit(0);
  });
});