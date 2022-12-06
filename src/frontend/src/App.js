import { useState } from "react";
import Login from "./components/Login";
import Poster from "./components/Poster";
import Timeline from "./components/Timeline";
function App() {
  const [username, setUsername] = useState("");
  return (
    <div className="App">
      {username == "" ? (
        <Login setUsername={setUsername}></Login>
      ) : (
        <div className="pt-12 flex items-center flex-col">
          <Poster></Poster>
          <Timeline></Timeline>
        </div>
      )}
    </div>
  );
}

export default App;
