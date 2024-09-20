console.log("welcome to holberton school, what is your name?")

process.stdin.on('data', (input) => {
	const name = input.toString().trim();

	console.log(`Your name is: ${name}`);

	console.log('This important software is now closing');
	
	process.exit();

});
