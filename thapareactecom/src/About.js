import React from "react";
import HeroSection from "./components/HeroSection";

const About = () => {
  const data = {
    name: "About Wayfarer",
  };

  return <HeroSection myData={data} />;
};

export default About;
