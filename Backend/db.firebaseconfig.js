var firebase = require('firebase');
var config = {
  apiKey: "AIzaSyAXyjuScWjrQraG5g7Kprgq3xlIG1XgFe8",
  authDomain: "codeflexersfirebase.firebaseapp.com",
  databaseURL: "https://codeflexersfirebase.firebaseio.com",
  projectId: "codeflexersfirebase",
  storageBucket: "codeflexersfirebase.appspot.com",
  messagingSenderId: "992811932100"
};
firebase.initializeApp(config);

module.exports = firebase;
