const http = require('http');
const port = 3001;

http.createServer((req, res) => {
    res.writeHead(200, {
        'Content-Type': 'text/plain',
    });
    res.statusCode = 200
    res.end('End of response\n');
}).listen(port);

console.log(`Server is running @ http://localhost:${port}`);