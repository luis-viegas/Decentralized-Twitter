import React from "react";
import axios from "axios";

function Following(props) {
  const [following, setFollowing] = React.useState([]);
  function getFollowing() {
    axios.get(`http://localhost:${props.port}/following`).then((response) => {
      let result = [];
      console.log(response.data);
      for (var i = 0; i < response.data.length; i++) {
        result.push(response.data[i]);
      }
      setFollowing(result);
    });
  }
  return (
    <div className="fixed bottom-0 right-0 border-2 rounded-xl border-blue-300 w-[20vw] h-[40vh] m-6 py-6 px-8">
      <div className="relative h-full flex flex-col">
        <h1 className="text-blue-300 font-bold uppercase text-xl ">
          Following
        </h1>
        <div className="flex-1 overflow-auto">
          <ul className="list-disc list-inside space-y-1 mt-6">
            {following.map((user, index) => (
              <li key={index} className="text-blue-300  ">
                {user}
              </li>
            ))}
          </ul>
        </div>
        <div className="flex justify-end  absolute top-0 right-0">
          <svg
            className="w-6 fill-blue-400 hover:fill-blue-700"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            onClick={() => getFollowing()}
          >
            <path d="M370.72 133.28C339.458 104.008 298.888 87.962 255.848 88c-77.458.068-144.328 53.178-162.791 126.85-1.344 5.363-6.122 9.15-11.651 9.15H24.103c-7.498 0-13.194-6.807-11.807-14.176C33.933 94.924 134.813 8 256 8c66.448 0 126.791 26.136 171.315 68.685L463.03 40.97C478.149 25.851 504 36.559 504 57.941V192c0 13.255-10.745 24-24 24H345.941c-21.382 0-32.09-25.851-16.971-40.971l41.75-41.749zM32 296h134.059c21.382 0 32.09 25.851 16.971 40.971l-41.75 41.75c31.262 29.273 71.835 45.319 114.876 45.28 77.418-.07 144.315-53.144 162.787-126.849 1.344-5.363 6.122-9.15 11.651-9.15h57.304c7.498 0 13.194 6.807 11.807 14.176C478.067 417.076 377.187 504 256 504c-66.448 0-126.791-26.136-171.315-68.685L48.97 471.03C33.851 486.149 8 475.441 8 454.059V320c0-13.255 10.745-24 24-24z" />
          </svg>
        </div>
      </div>
    </div>
  );
}

export default Following;
