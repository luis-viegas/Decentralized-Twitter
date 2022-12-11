import FakeTwitter from "./fake-twitter.png";
import React, { useState } from "react";
import axios from "axios";

function Login(props) {
  const [usernameInput, setUsernameInput] = useState("");
  const [passwordInput, setPasswordInput] = useState("");
  const [showAnimation, setShowAnimation] = useState(false);

  let [authMode, setAuthMode] = useState("signin");

  const changeAuthMode = () => {
    setAuthMode(authMode === "signin" ? "signup" : "signin");
  };

  function doLogin(usernameInput, passwordInput) {
    setShowAnimation(true);
    axios
      .post("http://localhost:8000/login", {
        username: usernameInput,
        password: passwordInput,
      })
      .then((response1) => {
        if (response1.status !== 200) {
          alert("Fail to login!");
        } else {
          const private_key = response1.data.private;
          const public_key = response1.data.public;

          axios
            .post(`http://localhost:${props.port}/login`, {
              username: usernameInput,
              private_key: private_key,
              public_key: public_key,
            })
            .then((response) => {
              props.setUsername(response.data);
              setShowAnimation(false);
            });
        }
      });
  }
  function doRegister(usernameInput, passwordInput) {
    axios
      .post("http://localhost:8000/create", {
        username: usernameInput,
        password: passwordInput,
      })
      .then((response) => {
        if (response.status !== 200) {
          alert("Fail to login!");
        } else {
          changeAuthMode();
        }
      });
  }

  return (
    <section>
      <h1 className="text-7xl uppercase text-center text-blue-400 py-16">
        Decentralized timeline
      </h1>
      <div className="container px-6 py-12 h-full">
        <div className="flex justify-center items-center flex-wrap h-full g-6 text-gray-800">
          <div className="md:w-8/12 lg:w-6/12 mb-12 md:mb-0">
            <img
              src={FakeTwitter}
              className="w-full filtro"
              alt="Phone image"
            />
          </div>
          <div className="md:w-8/12 lg:w-5/12 lg:ml-20">
            <div>
              <div>
                <h4 className="text-4xl text-center text-blue-400 py-16">
                  {authMode === "signin" ? "Sign In" : "Sign Up"}
                </h4>
              </div>
              <div className="mb-6">
                <input
                  type="text"
                  className="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-400 focus:outline-none"
                  placeholder="Username"
                  onChange={(e) => setUsernameInput(e.target.value)}
                />
              </div>
              <div className="mb-6">
                <input
                  type="password"
                  className="form-control block w-full px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-400 focus:outline-none"
                  placeholder="Password"
                  onChange={(e) => setPasswordInput(e.target.value)}
                />
              </div>
              {authMode === "signin" ? (
                <>
                  <button
                    className="inline-block px-7 py-3 bg-blue-400 text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out w-full"
                    data-mdb-ripple="true"
                    data-mdb-ripple-color="light"
                    onClick={() => doLogin(usernameInput, passwordInput)}
                  >
                    Sign in
                    {showAnimation && (
                      <div className="lds-ring">
                        <div></div>
                        <div></div>
                        <div></div>
                        <div></div>
                      </div>
                    )}
                  </button>
                  <div className="text-center">
                    Not registered yet?{" "}
                    <span className="link-primary" onClick={changeAuthMode}>
                      <a
                        href="#!"
                        className="underline text-blue-600 hover:text-blue-700"
                      >
                        Sign Up
                      </a>
                    </span>
                  </div>
                </>
              ) : (
                <>
                  <button
                    className="inline-block px-7 py-3 bg-blue-400 text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out w-full"
                    data-mdb-ripple="true"
                    data-mdb-ripple-color="light"
                    onClick={() => doRegister(usernameInput, passwordInput)}
                  >
                    Sign up
                  </button>
                  <div className="text-center">
                    Already registered?{" "}
                    <span className="link-primary" onClick={changeAuthMode}>
                      <a
                        href="#!"
                        className="underline text-blue-600 hover:text-blue-700"
                      >
                        Sign In
                      </a>
                    </span>
                  </div>
                </>
              )}
            </div>
          </div>
        </div>
      </div>
      <input
        type="number"
        placeholder="write your port value here (1 - 100)"
        onChange={(e) => {
          props.setPort(5000 + Number(e.target.value));
        }}
        className="ml-[25vw] w-1/2 px-4 py-2 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-400 focus:outline-none"
      ></input>
    </section>
  );
}

export default Login;
