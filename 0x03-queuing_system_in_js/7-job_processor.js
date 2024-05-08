import { createQueue } from "kue";

// Create a new Kue queue that process two jobs at a time
const queue = createQueue({ concurrency: 2 });

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  // Track the progress of the job of 0 out of 100
  job.progress(0, 100);

  if (blacklist.includes(phoneNumber)) {
    return done(Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track the progress of the job of 50 out of 100
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Process the job
queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
