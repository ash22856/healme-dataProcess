const {Pool} = require('pg')

const pool = new Pool({
user: "aeronchen",
host: "localhost",
database: "test",
password: "zs88920040",
port: "5432"
})

pool.connect()
// String for the PostgreSQL table name

const query = 'CREATE TABLE persons(email VARCHAR, firstName VARCHAR, lastName VARCHAR, age INT);'

const values = [
    'xxx@gmail.com',
    'Aeron',
    'liu',
    20
]
const tableName = 'persons'
// Declare a Template literal string for the SQL statement
let sqlString = `
INSERT INTO ${tableName}
(email, firstName, lastName, age)
VALUES
($1, $2, $3, $4)`

// Pass the string and array to the pool's query() method
pool.query(sqlString, values, (err, res) => {
if (err) {
console.log('pool.query():', err)
}

if (res) {
console.log('pool.query():', res)
}
})

// const ageQuery = 20
// const selectQuery = `SELECT * FROM ${tableName} WHERE gender = $male`

// // Pass the string and integer to the pool's query() method
// pool.query(selectQuery, [ageQuery], (err, res) => {
// if (err) {
// console.log('SELECT pool.query():', err)
// }

// if (res) {
// console.log('SELECT pool.query():', res)
// }
// })

pool.end()