import React from "react";

function Tweet(props) {
  return (
    <li>
      <div className="flex flex-start items-center">
        <div className="bg-blue-400 w-4 h-4 flex items-center justify-center rounded-full -ml-2 mr-3 -mt-2"></div>
        <h4 className="text-gray-800 font-semibold text-xl -mt-2">
          {props.username || "Elon Musk"}
        </h4>
      </div>
      <div className="ml-6 mb-6 pb-6">
        <p
          href="#!"
          className="text-blue-400 hover:text-blue-700 focus:text-blue-800 duration-300 transition ease-in-out text-sm"
        >
          4 February, 2022
        </p>
        <p className="text-gray-700 mt-2 mb-4 text-left">
          {props.tweet ||
            "I am the real Elon Musk... Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed doeiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim adminim veniam, quis nostrud exercitation ullamco laboris nisi ut"}
        </p>
      </div>
    </li>
  );
}

export default Tweet;
