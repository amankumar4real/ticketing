import React from "react";
import {Route} from "react-router-dom";
import GoogleMap from "../GoogleMap/GoogleMap"

const Routers = () => {
  return(
      <div>
        <Route path="/" exact component ={GoogleMap}/>
      </div>
  )
}

export default Routers;