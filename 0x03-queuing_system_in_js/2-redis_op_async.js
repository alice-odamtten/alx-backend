import redis from 'redis';
import { promisify } from "util";

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  get(schoolName).then((res) => {
    console.log(res);
  });
}

process.on('SIGINT', () => {
  client.quit();
  process.exit();
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
