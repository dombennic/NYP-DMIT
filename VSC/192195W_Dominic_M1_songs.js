const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/MySongsDB', {useNewUrlParser: true, useUnifiedTopology: true});

const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));

db.once("open", function() {
  console.log("Connection Successful!");
});

const songsSchema = new mongoose.Schema({
    // _id: ObjectId (""),
    title: String,
    album: String,  
    duration: String,
    artist: String,
    releaseDate: String,
  });

const artistsSchema = new mongoose.Schema({
    // _id: ObjectId (""),
    name: String,
    debut: Int32Array,
    profilePic: String,     
  });  

const artists = mongoose.model('artists', artistsSchema);

const songs = mongoose.model('songs', songsSchema);

songs.find(function (err, songs) {
    if (err) return console.error(err);
    console.log(songs);
  })

artists.find(function (err, artists) {
    if (err) return console.error(err);
    console.log(artists);
  })