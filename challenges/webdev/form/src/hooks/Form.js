import React, { useState } from "react";

const table = [
  { qst: "who are you", input: "drop your name" },
  { qst: "how to contact you", input: "drop your email" },
  { qst: "how old are you", input: "drop your age" },
];

function Form() {
  var [index, setstate] = useState(0);
  var data = table[index];
  return (
    <div className="form">
      <h3> {index}/14</h3>
      <h1>{data.qst}</h1>
      <input type="text" placeholder={data.input} />

      {index < 3 ? (
        <button
          onClick={() => {
            setstate(index + 1);
            console.log("here");
          }}
        >
          Next
        </button>
      ) : (
        ""
      )}
    </div>
  );
}

export default Form;
