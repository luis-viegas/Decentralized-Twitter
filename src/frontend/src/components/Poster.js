import React from "react";
import axios from "axios";
function Poster(props) {
  const [tweet, setTweet] = React.useState("");
  function doTweet() {
    axios
      .post(`http://localhost:${props.port}/tweet`, {
        text: tweet,
      })
      .then((response) => {
        window.alert(response.data);
        console.log(response);
      });
  }
  return (
    <div className="block p-12 rounded-lg shadow-lg bg-white flex justify-between w-[50vw]">
      <img
        src="https://pyxis.nymag.com/v1/imgs/34c/cae/ce8997338cbad42766ca705559b6e0ad6f-elon-musk-.rsquare.w700.jpg"
        className="rounded-full w-16 h-16"
      />
      <div className="flex justify-center items-end ml-6 w-full flex-col">
        <input
          type="text"
          className="form-control block mb-5 w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
          id="exampleFormControlInput2"
          placeholder="Tweet something..."
          onChange={(e) => setTweet(e.target.value)}
        />
        <button
          type="button"
          className="inline-block px-7 py-3 bg-blue-400 text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
          onClick={() => doTweet()}
        >
          Tweet
        </button>
      </div>
    </div>
  );
}

export default Poster;
