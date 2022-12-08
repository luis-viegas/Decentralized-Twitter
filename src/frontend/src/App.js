import { useState } from "react";
import Login from "./components/Login";
import Poster from "./components/Poster";
import Timeline from "./components/Timeline";
import Follower from "./components/Follower";
function App() {
  const [username, setUsername] = useState("");
  return (
    <div className="App">
      {username === "" ? (
        <Login setUsername={setUsername}></Login>
      ) : (
        <div className="pt-4 flex items-center flex-col">
          <Follower></Follower>
          <Poster></Poster>
          <Timeline></Timeline>
        </div>
      )}
    </div>
  );
}

export default App;
