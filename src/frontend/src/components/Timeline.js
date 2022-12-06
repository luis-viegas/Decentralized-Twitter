import React from "react";
import Tweet from "./Tweet";

function Timeline() {
  return (
    <div className="w-[50vw] mt-16">
      <ol className="border-l-2 border-blue-400">
        <Tweet />
        <Tweet />
        <Tweet />
      </ol>
    </div>
  );
}

export default Timeline;
