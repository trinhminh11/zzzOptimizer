import React from "react";
import WEngineLocalDatabase from "./WEngineLocalDatabase";
import WEngineDatabase from "./WEngineDatabase";
import "./wEngine.css";

function WEngineBody() {
  return (
    <div className="row wEngine-body">
      <div className="col-lg-3">
        <WEngineLocalDatabase />
      </div>
      <div className="col-lg-9">
        <WEngineDatabase />
      </div>
    </div>
  );
}

export default WEngineBody;
