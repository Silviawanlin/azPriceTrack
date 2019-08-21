const Pool = require('pg').Pool
const pool = new Pool({
  user: process.ENV.AWS_POSTGRES_USER,
  host: process.ENV.AWS_POSTGRES_URL,
  database: 'azpricecheck',
  password: process.ENV.AWS_POSTGRES_PASSWORD,
  port: 5432,
})


pool.query('SELECT * FROM UserAccount', (error, results) => {
    if (error) {
      throw error
    }
    console.log(results);
  });

