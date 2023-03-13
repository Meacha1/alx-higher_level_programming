#!/usr/bin/node
const count = process.argv.length;

if (count == 2)
{
	console.log('No argument');
}
if (count == 3)
{
	console.log('Argument found');
}
if (count > 3)
{
	console.log('Arguments found');
}
