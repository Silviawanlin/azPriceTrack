const Pool = require('pg').Pool
const pool = new Pool({
  user: 'gavin0228',
  host: 'gavindb.cblluydijtdx.us-east-1.rds.amazonaws.com',
  database: 'azpricecheck',
  password: 'lang8524560',
  port: 5432,
})
