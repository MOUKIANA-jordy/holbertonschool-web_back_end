const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.trim().split('\n');
      const students = lines.slice(1);

      if (students.length === 0) {
        console.log('Number of students: 0');
        resolve();
        return;
      }

      const studentData = {};
      let totalStudents = 0;

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (firstname && field) {
          totalStudents += 1;
          if (!studentData[field]) {
            studentData[field] = [];
          }
          studentData[field].push(firstname);
        }
      });

      console.log(`Number of students: ${totalStudents}`);
      for (const [field, names] of Object.entries(studentData)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
