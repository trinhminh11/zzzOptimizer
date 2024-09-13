import React from "react";
import "./agent.css";
import AgentLocalDatabase from "./agentLocalDatabase";
import AgentDatabase from "./agentDatabase";
import { AgentsService } from "../../services/AgentService";
import { useState, useEffect } from "react";

function AgentBody({ selectedOptions, setSelectedOptions }) {
  // set up list for storing agent from api
  const [listAgents, setListAgents] = useState([]);

  // set up localstorage for storing infomation
  const [listSelectedAgents, setListSelectedAgents] = useState(() => {
    // Check local storage and initialize list
    const storedAgents = localStorage.getItem("agents");
    return storedAgents ? JSON.parse(storedAgents) : [];
  });

  // Set up function to store data from api into the list
  useEffect(() => {
    getAgents();
  }, []);

  const getAgents = async () => {
    let res = await AgentsService();
    if (res) {
      // Add new mindScape attribute
      for (let i = 0; i < res.length; i++) {
        res[i].mindScape = 0;
        res[i].promotion = 0;
        res[i].skills = {
          level: 1,
          core: 1,
          basic: 1,
          dodge: 1,
          assist: 1,
          special: 1,
          chain: 1
        }
      }
      setListAgents(res);
    }
  };

  return (
    <div className="row agent-body">
      <div className="col-lg-3">
        <AgentDatabase
          listAgents={listAgents}
          listSelectedAgents={listSelectedAgents}
          setListSelectedAgents={setListSelectedAgents}
          selectedOptions={selectedOptions}
          setSelectedOptions={setSelectedOptions}
        />
      </div>
      <div className="col-lg-9">
        <AgentLocalDatabase
          listSelectedAgents={listSelectedAgents}
          setListSelectedAgents={setListSelectedAgents}
          selectedOptions={selectedOptions}
        />
      </div>
    </div>
  );
}

export default AgentBody;
