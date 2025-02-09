// What’s wrong with the code style below?

function pow(x,n)                               // no space
{                                               // bracket on separate line
    let result=1;                               // no spaces around `=`
    for(let i=0;i<n;i++) {result*=x;}           // no spaces
    return result;
}

let x=prompt("x?",''), n=prompt("n?",'')        // two commands on one line
if (n<=0)                                       // no spaces around `<=`
{                                               // separate bracket
    alert(`Power ${n} is not supported, please enter an integer number greater than zero`);
}
else
{                                               // better to write `} else {`
    alert(pow(x,n))
}
