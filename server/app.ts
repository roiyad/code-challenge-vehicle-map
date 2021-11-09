import express from 'express'
import vehicles from './vehicles-location.json';

const app = express();
const port = 8080;

app.get('/', (req, res) => {
    res.send(vehicles);
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});

