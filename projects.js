// Each project is one entry. Add new projects to the top of the list.
window.PROJECTS = [
  {
    title: "Xylella Watch",
    tagline: "Tracking the spread of Xylella fastidiosa across Mediterranean olive groves",
    summary:
      "An interactive map that combines satellite signs of olive-grove decline with official records of " +
      "Xylella fastidiosa, the bacterium that has killed millions of olive trees in southern Italy and " +
      "is still spreading around the Mediterranean.",
    highlights: [
      "Weekly 10 m Sentinel-2 scans of selected regions compare each summer's OSAVI greenness with the year before, filtering out buildings, irrigated and rotating crops, and areas that recover.",
      "A yearly 100 m screen of the whole Mediterranean olive belt, split into 1° cells that run as parallel GitHub Actions jobs, with wildfire scars (NASA MODIS) removed.",
      "Official records from EPPO, the European Commission and regional plant-health services, with a year slider to replay the spread and rings showing projected natural spread.",
      "Automated weekly checks of EPPO, official sources and new research (OpenAlex) that open GitHub issues for a person to review. Nothing goes on the map without review.",
      "Crop profiles for olive, almond and grapevine, using farm-parcel registers as masks, plus a public form where anyone can suggest an official source to watch."
    ],
    stack: ["Python", "Streamlit", "Folium", "Sentinel-2", "GitHub Actions", "pandas", "NumPy / SciPy", "pytest"],
    links: [
      { label: "Live app", url: "https://xylella-tracker.streamlit.app/" },
      { label: "Source code", url: "https://github.com/humanismContributor/Xylella-Fastidiosa-tracker" }
    ],
    note: "Detection thresholds come from published studies, not field calibration. A flagged area is a lead for inspection, not a diagnosis."
  }
];
