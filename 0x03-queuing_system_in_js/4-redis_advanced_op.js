import { createClient, print } from "redis";

const client = createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
});
client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});


const entries = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

Object.entries(entries).forEach(([key, value]) => {
  client.hset('HolbertonSchools', key, value, print);
});

client.hgetall('HolbertonSchools', (err, res) => {
  console.log(res);
});
