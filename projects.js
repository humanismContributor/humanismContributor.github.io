// Each project is one entry. Add new projects to the top of the list.
// Optional fields: images (chart gallery), youtube (the video ID, e.g. "dQw4w9WgXcQ"), note.
window.PROJECTS = [
  {
    title: "AI Adoption Across Countries and Industries",
    tagline: "Exploratory data analysis in R of 145,000 records of AI tool adoption",
    summary:
      "An exploratory analysis of how AI tools such as ChatGPT, Midjourney, Stable Diffusion, Bard and Claude " +
      "are adopted across 10 countries, 8 industries, 5 age groups and 3 company sizes in 2023 and 2024. " +
      "It looks for which groups adopt AI fastest and how adoption changed from one year to the next.",
    highlights: [
      "Prepared the data with tidyverse, turning age group, company size and year into ordered factors so every chart reads in a natural order.",
      "Compared mean adoption rate and daily active users by company size, age group, industry, country and year, using bar charts, ridgeline density plots, line charts, heatmaps and per-country facets, combined into dashboards with patchwork.",
      "Ranked the top 20 country × industry × company size × age group combinations and exported them as a summary table.",
      "Main finding: adoption barely varies. Every group averages between 49.5 % and 50.3 %, and rates are spread evenly from 0 to 100 %. Most of the variation is in which tools people use: ChatGPT appears in 40 % of records, Claude in 5 %.",
      "That flatness, together with random-text user feedback, shows the dataset is synthetic. A key lesson was to check the scale of a difference before reading a trend into it."
    ],
    stack: ["R", "tidyverse", "ggplot2", "ggridges", "patchwork", "Data visualisation"],
    images: [
      { src: "projects/ai-adoption/country_analysis.png", alt: "Bar chart of mean AI adoption by country next to a heatmap of country by AI tool" },
      { src: "projects/ai-adoption/company_size_analysis.png", alt: "Adoption by company size: bar chart, ridgeline distribution and per-tool bars" },
      { src: "projects/ai-adoption/industry_analysis.png", alt: "Adoption by industry and an industry by AI tool heatmap" },
      { src: "projects/ai-adoption/age_group_analysis.png", alt: "Adoption across age groups, by tool, and an age by company size heatmap" },
      { src: "projects/ai-adoption/yoy_trends.png", alt: "Year-over-year adoption from 2023 to 2024 by company size, industry and age group" }
    ],
    links: [
      { label: "R script", url: "projects/ai-adoption/analysis.R" }
    ]
  },
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
