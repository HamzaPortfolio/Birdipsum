exports.handler = async () => {
  const classes = {
    df: "display: flex;",
    db: "display: block;",
    dib: "display: inline-block;",
    jc-ctr: "justify-content: center;",
    ai-ctr: "align-items: center;",
    clr-black: "color: black;",
    clr-white: "color: white;",
    bg-red: "background-color: red;",
    bg-blue: "background-color: blue;"
  };

  let cssOutput = "";

  for (const className in classes) {
    cssOutput += `.${className} { ${classes[className]} }
`;
  }

  return {
    statusCode: 200,
    headers: { "Content-Type": "text/css" },
    body: cssOutput
  };
};