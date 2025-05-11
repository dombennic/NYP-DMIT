const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test', {useNewUrlParser: true, useUnifiedTopology: true});


const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  // we're connected!
});


const songSchema = new mongoose.Schema({
    title:String,
    album:String,
    duration:String,
    artist:String,
    releaseDate:String

});

const song = mongoose.model('song', songSchema);

song.find(function (err, song) {
    if (err) return console.error(err);
    console.log(song);
  })

song.find({ title:"My Love" }, callback);