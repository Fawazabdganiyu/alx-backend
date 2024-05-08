import { createClient } from "redis";
import { Job, createQueue } from "kue";
import express from "express";
import { promisify } from "util";

// Redis client
const client = createClient();
const getAsync = promisify(client.get).bind(client);

function reserveSeat(number) {
  client.set('available_seats', number);
}

function getCurrentAvailableSeats() {
  return getAsync('available_seats');
}

// Initialize max available seats
reserveSeat(50);

// Initialize reservation status
let reservationEnabled = true;

// Kue queue
const queue = createQueue();

// Express server
const app = express();

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
      return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  })
  .on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: ' Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats <= 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      reserveSeat(availableSeats - 1);
      done();
    }
  });
});

app.listen(1245);
