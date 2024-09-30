import axios from "./customize_axios";

//Get all WEngines
function DriveDiscService() {
  return axios.get("/drivediscs");
}

export { DriveDiscService };
