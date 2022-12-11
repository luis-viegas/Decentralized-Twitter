import { useState } from "react";
import Login from "./components/Login";
import Poster from "./components/Poster";
import Timeline from "./components/Timeline";
import Follower from "./components/Follower";
import Following from "./components/Following";
import axios from "axios";
function App() {
  const [username, setUsername] = useState("");
  const [port, setPort] = useState(5001);

  function doLogout() {
    axios.get(`http://localhost:${port}/logout`, {}).then((response) => {
      window.alert(response.data);
      setUsername("");
    });
  }
  return (
    <div className="App">
      {username === "" ? (
        <Login setUsername={setUsername} setPort={setPort} port={port}></Login>
      ) : (
        <div className="pt-4 flex items-center flex-col">
          <div className="flex justify-between w-full px-24">
            <h1 className="text-xl text-blue-400">{username}</h1>
            <button
              type="button"
              className="inline-block px-7 py-3 bg-blue-400 text-white font-medium text-sm leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
              onClick={() => doLogout()}
            >
              Logout
            </button>
          </div>

          <Follower port={port}></Follower>
          <Poster port={port}></Poster>
          <Timeline port={port}></Timeline>
          <Following port={port}></Following>
        </div>
      )}
    </div>
  );
}

export default App;
