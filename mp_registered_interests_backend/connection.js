const MongoClient = require("mongodb").MongoClient;

const uri =
  "mongodb+srv://admin:fJWP9TaqQRKV08YQ@cluster0.usilp.mongodb.net/interests_production?retryWrites=true&w=majority";

const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const connection = client.connect();
module.exports = client;
