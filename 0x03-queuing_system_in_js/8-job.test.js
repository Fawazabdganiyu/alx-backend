import { createQueue } from "kue";
import { expect } from "chai";
import sinon from "sinon";

import createPushNotificationsJobs from "./8-job";

let queue = createQueue();
let consoleSpy;

describe("createPushNotificationsJobs", () => {
  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error with an invalid jobs argument', () => {
    expect(() => createPushNotificationsJobs('test', queue)).to.throw('Jobs is not an array');
  });

  it("should create two jobs successfully", () => {
    const list = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
      {
        phoneNumber: "4153518781",
        message: "This is the code 4562 to verify your account",
      },
    ];

    createPushNotificationsJobs(list, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.deep.equal(list[0]);
    expect(queue.testMode.jobs[1].data.phoneNumber).to.equal(list[1].phoneNumber);
  });

  it("should not create any jobs with an empty list", () => {
    const list = [];
    
    createPushNotificationsJobs(list, queue);
    
    expect(queue.testMode.jobs.length).to.equal(0);
  });
});
