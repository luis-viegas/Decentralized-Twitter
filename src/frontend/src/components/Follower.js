import React from "react";
import axios from "axios";
function Follower(props) {
  const [username, setUsername] = React.useState("");
  function doFollow() {
    axios
      .post(`http://localhost:${props.port}/follow`, {
        username: username,
      })
      .then((response) => {
        window.alert(response.data);
        console.log(response);
      });
  }
  function doUnfollow() {
    axios
      .post(`http://localhost:${props.port}/unfollow`, {
        username: username,
      })
      .then((response) => {
        window.alert(response.data);
        console.log(response);
      });
  }
  return (
    <div className="block pt-8 pb-6 px-6 mb-10 rounded-lg shadow-lg bg-white flex justify-between w-[50vw]">
      <div className="flex justify-center items-end  w-full flex-col">
        <input
          type="text"
          className="form-control block mb-3 w-full px-3 py-2 text-sm font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
          id="exampleFormControlInput2"
          placeholder="Follow or unfollow someone..."
          onChange={(e) => setUsername(e.target.value)}
        />
        <div>
          <button
            type="button"
            className="inline-block px-5 py-2 mr-4 bg-green-400 text-white font-medium text-xs leading-snug uppercase rounded shadow-md hover:bg-green-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            onClick={() => doFollow()}
          >
            Follow
          </button>
          <button
            type="button"
            className="inline-block px-5 py-2 bg-red-400 text-white font-medium text-xs leading-snug uppercase rounded shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
            onClick={() => doUnfollow()}
          >
            Unfollow
          </button>
        </div>
      </div>
    </div>
  );
}

export default Follower;
