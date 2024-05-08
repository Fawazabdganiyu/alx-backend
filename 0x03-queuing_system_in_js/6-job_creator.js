import { createQueue } from "kue";

const queue = createQueue();

const jobData = {
  phoneNumber: "+234567890",
  message: "This is the code to verify your account",
};

const job = queue.create("push_notification_code", jobData);

job.on("enqueue", () => {
  console.log(`Notification job created: ${job.id}`);
})
.on("complete", () => {
  console.log("Notification job completed");
})
.on("failed", () => {
  console.log("Notification job failed");
})
.save();
