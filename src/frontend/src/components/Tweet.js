import React from "react";

function Tweet(props) {
  function convertTime(time) {
    time = time;
    console.log(time);
    let month = time[1];
    let day = time[2];
    let year = time[0];
    let hour = time[3];
    let minute = time[4];
    if (minute < 10) minute = "0" + minute;
    return day + "/" + month + "/" + year + " " + hour + ":" + minute;
  }
  return (
    <li>
      <div className="flex flex-start items-center">
        <div className="bg-blue-400 w-4 h-4 flex items-center justify-center rounded-full -ml-2 mr-3 -mt-2"></div>
        <h4 className="text-gray-800 font-semibold text-xl -mt-2">
          {props.username || "Unnamed user"}
        </h4>
      </div>
      <div className="ml-6 mb-6 pb-6">
        <p
          href="#!"
          className="text-blue-400 hover:text-blue-700 focus:text-blue-800 duration-300 transition ease-in-out text-sm"
        >
          {convertTime(props.time) || "4 February, 2022"}
        </p>
        <p className="text-gray-700 mt-2 mb-4 text-left">
          {props.text || "Unable to get tweet text"}
        </p>
      </div>
    </li>
  );
}

export default Tweet;
