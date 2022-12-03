// Example POST method implementation:
const lexicalAnalysis = async(sentence) => {
        // Default options are marked with *
        const response = await fetch("http://localhost:8000/lexicAnalysis", {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            headers: {
              'Content-Type': 'application/json'
              // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            redirect: 'follow', // manual, *follow, error
            referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
            body: JSON.stringify({
              "sentence": sentence
            }) // body data type must match "Content-Type" header
      
          }).then((R)=>{
              return R.json();
          });
          return response
}

const syntaxAnalysis = async(sentence) => {
    // Default options are marked with *
    const response = await fetch("http://localhost:8000/syntaxAnalysis", {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify({
        "sentence": sentence
        }) // body data type must match "Content-Type" header

    }).then((R)=>{
        return R.json();
    });
    return response
}
