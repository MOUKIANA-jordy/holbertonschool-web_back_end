const countStudents = require('./3-read_file_async');

countStudents("nope.csv")
    .then(() => {
        console.log("Done!");
    })
        .catch((error) => {
        console.log(error);
    });

bob@dylan:~$ node 3-main_0.js
Error: Cannot load the database
...
