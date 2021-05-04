const MongoClient = require("mongodb").MongoClient;
const fs = require("fs");

const uriMembersTest =
  "mongodb+srv://admin:fJWP9TaqQRKV08YQ@cluster0.usilp.mongodb.net/members_test?retryWrites=true&w=majority";

async function main() {
  const client = new MongoClient(uriMembersTest, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  propertyToAdd = { clicks: 0 };

  try {
    await client.connect();
    await addProperty(client, propertyToAdd);
  } catch (e) {
    console.error(e);
  } finally {
    await client.close();
  }
}

main().catch(console.error);

async function addProperty(client, propertyToAdd) {
  result = await client
    .db("mp_registered_interests")
    .collection("members_test")
    .updateMany({}, { $set: propertyToAdd }, false, true);

  console.log(`RESULT = ${result}`);
}
