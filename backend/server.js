const express = require('express')
const priceRouter = require('./routers/price')
const userRouter = require('./routers/user')
const app = express()

app.get('/', (req, res) => res.send('Hello World!'));


app.use('/user', userRouter );

app.use('/price', priceRouter);

app.listen( 3000, "0.0.0.0", () => console.log(`Example app listening on port 3000!`))