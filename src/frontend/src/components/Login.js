import FakeTwitter from "./fake-twitter.jpg";
import React, { useState } from "react";
import axios from "axios";

function doLogin(usernameInput) {
  axios
    .post("http://localhost:5001/login", { username: usernameInput })
    .then((response) => {
      console.log(response);
    });
}

function doTweet() {
  axios
    .post("http://localhost:5001/tweet", {
      username: "test",
      tweet: "test tweet",
    })
    .then((response) => {
      console.log(response);
    });
}

function Login() {
  const [usernameInput, setUsernameInput] = useState("");
  return (
    <section>
      <h1 className="text-7xl uppercase text-blue-400 py-16">
        Decentralized timeline
      </h1>
      <div class="container px-6 py-12 h-full">
        <div class="flex justify-center items-center flex-wrap h-full g-6 text-gray-800">
          <div class="md:w-8/12 lg:w-6/12 mb-12 md:mb-0">
            <img src={FakeTwitter} class="w-full" alt="Phone image" />
          </div>
          <div class="md:w-8/12 lg:w-5/12 lg:ml-20">
            <div>
              <div class="mb-6">
                <input
                  type="text"
                  class="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-400 focus:outline-none"
                  placeholder="Username"
                  onChange={(e) => setUsernameInput(e.target.value)}
                />
              </div>

              <button
                class="inline-block px-7 py-3 bg-blue-400 text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out w-full"
                data-mdb-ripple="true"
                data-mdb-ripple-color="light"
                onClick={() => doLogin(usernameInput)}
              >
                Sign in
              </button>
              <button
                class="inline-block px-7 py-3 bg-blue-400 text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out w-full"
                data-mdb-ripple="true"
                data-mdb-ripple-color="light"
                onClick={() => doTweet()}
              >
                Tweet
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Login;
