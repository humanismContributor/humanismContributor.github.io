# AI Adoption Across Countries, Industries and Demographics
# Exploratory analysis of a 145,000-row dataset of AI tool adoption (2023–2024).
# Expects ai_adoption_dataset.csv in the working directory.

library(tidyverse)
library(scales)
library(patchwork)
library(ggridges)

# ---- Load & prepare data ----------------------------------------------------
df <- read_csv("ai_adoption_dataset.csv", show_col_types = FALSE)

df <- df %>%
  mutate(
    age_group    = factor(age_group,    levels = c("18-24", "25-34", "35-44", "45-54", "55+")),
    company_size = factor(company_size, levels = c("Startup", "SME", "Enterprise")),
    year         = factor(year)
  )

glimpse(df)
summary(df)


# ---- Company size -----------------------------------------------------------
size_adoption <- df %>%
    group_by(company_size) %>%
    summarise(
        mean_adoption = mean(adoption_rate),
        mean_dau      = mean(daily_active_users),
        n             = n(),
        .groups = "drop"
    )
print(size_adoption)

p1a <- ggplot(size_adoption, aes(x = company_size, y = mean_adoption, fill = company_size)) +
    geom_bar(stat = "identity", width = 0.6, show.legend = FALSE) +
    geom_text(aes(label = round(mean_adoption, 1)), vjust = -0.5, fontface = "bold") +
    scale_fill_brewer(palette = "Set2") +
    labs(title = "Average AI Adoption Rate by Company Size",
         x = "Company Size", y = "Mean Adoption Rate (%)") +
    theme_minimal(base_size = 13)

p1b <- ggplot(df, aes(x = adoption_rate, y = company_size, fill = company_size)) +
    geom_density_ridges(alpha = 0.7, show.legend = FALSE) +
    scale_fill_brewer(palette = "Set2") +
    labs(title = "Adoption Rate Distribution by Company Size",
         x = "Adoption Rate (%)", y = NULL) +
    theme_minimal(base_size = 13)

size_tool <- df %>%
    group_by(company_size, ai_tool) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop")

p1c <- ggplot(size_tool, aes(x = ai_tool, y = mean_adoption, fill = company_size)) +
    geom_bar(stat = "identity", position = "dodge") +
    scale_fill_brewer(palette = "Set2") +
    labs(title = "AI Tool Adoption by Company Size",
         x = "AI Tool", y = "Mean Adoption Rate (%)", fill = "Company Size") +
    theme_minimal(base_size = 13) +
    theme(axis.text.x = element_text(angle = 30, hjust = 1))

(p1a | p1b) / p1c
ggsave("company_size_analysis.png", width = 14, height = 12, dpi = 120)


# ---- Age group --------------------------------------------------------------
age_adoption <- df %>%
    group_by(age_group) %>%
    summarise(
        mean_adoption = mean(adoption_rate),
        mean_dau      = mean(daily_active_users),
        .groups = "drop"
    )
print(age_adoption)

p2a <- ggplot(age_adoption, aes(x = age_group, y = mean_adoption, group = 1)) +
    geom_line(color = "#2196F3", linewidth = 1.2) +
    geom_point(color = "#2196F3", size = 4) +
    geom_text(aes(label = round(mean_adoption, 1)), vjust = -1, fontface = "bold") +
    labs(title = "AI Adoption Rate Across Age Groups",
         x = "Age Group", y = "Mean Adoption Rate (%)") +
    theme_minimal(base_size = 13)

age_tool <- df %>%
    group_by(age_group, ai_tool) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop")

p2b <- ggplot(age_tool, aes(x = age_group, y = mean_adoption, color = ai_tool, group = ai_tool)) +
    geom_line(linewidth = 1.1) +
    geom_point(size = 3) +
    scale_color_brewer(palette = "Dark2") +
    labs(title = "AI Tool Adoption by Age Group",
         x = "Age Group", y = "Mean Adoption Rate (%)", color = "AI Tool") +
    theme_minimal(base_size = 13)

age_size_heat <- df %>%
    group_by(age_group, company_size) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop")

p2c <- ggplot(age_size_heat, aes(x = company_size, y = age_group, fill = mean_adoption)) +
    geom_tile(color = "white", linewidth = 0.8) +
    geom_text(aes(label = round(mean_adoption, 1)), fontface = "bold") +
    scale_fill_gradient(low = "#e3f2fd", high = "#1565C0") +
    labs(title = "Adoption Rate Heatmap: Age Group × Company Size",
         x = "Company Size", y = "Age Group", fill = "Mean\nAdoption (%)") +
    theme_minimal(base_size = 13)

(p2a | p2b) / p2c
ggsave("age_group_analysis.png", width = 14, height = 14, dpi = 120)


# ---- Industry ---------------------------------------------------------------
industry_adoption <- df %>%
    group_by(industry) %>%
    summarise(
        mean_adoption = mean(adoption_rate),
        mean_dau      = mean(daily_active_users),
        .groups = "drop"
    ) %>%
    arrange(desc(mean_adoption))
print(industry_adoption)

p3a <- ggplot(industry_adoption,
              aes(x = reorder(industry, mean_adoption), y = mean_adoption, fill = mean_adoption)) +
    geom_bar(stat = "identity", show.legend = FALSE) +
    geom_text(aes(label = round(mean_adoption, 1)), hjust = -0.2, fontface = "bold") +
    scale_fill_gradient(low = "#b2dfdb", high = "#00695c") +
    coord_flip() +
    labs(title = "AI Adoption Rate by Industry",
         x = NULL, y = "Mean Adoption Rate (%)") +
    theme_minimal(base_size = 13)

industry_tool <- df %>%
    group_by(industry, ai_tool) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop")

p3b <- ggplot(industry_tool, aes(x = ai_tool, y = industry, fill = mean_adoption)) +
    geom_tile(color = "white", linewidth = 0.8) +
    geom_text(aes(label = round(mean_adoption, 1)), fontface = "bold") +
    scale_fill_gradient(low = "#f3e5f5", high = "#6a1b9a") +
    labs(title = "AI Tool Adoption Heatmap: Industry × Tool",
         x = "AI Tool", y = NULL, fill = "Mean\nAdoption (%)") +
    theme_minimal(base_size = 13)

p3a / p3b
ggsave("industry_analysis.png", width = 13, height = 12, dpi = 120)


# ---- Geography --------------------------------------------------------------
country_adoption <- df %>%
    group_by(country) %>%
    summarise(
        mean_adoption = mean(adoption_rate),
        mean_dau      = mean(daily_active_users),
        .groups = "drop"
    ) %>%
    arrange(desc(mean_adoption))
print(country_adoption)

p4a <- ggplot(country_adoption,
              aes(x = reorder(country, mean_adoption), y = mean_adoption, fill = mean_adoption)) +
  geom_bar(stat = "identity", show.legend = FALSE) +
  geom_text(aes(label = round(mean_adoption, 1)), hjust = -0.2, fontface = "bold") +
  scale_fill_gradient(low = "#fff9c4", high = "#f57f17") +
  coord_flip(clip = "off") +
  scale_y_continuous(limits = c(0, max(country_adoption$mean_adoption) * 1.15)) +
  labs(title = "AI Adoption Rate by Country",
       x = NULL, y = "Mean Adoption Rate (%)") +
  theme_minimal(base_size = 13)

country_tool <- df %>%
    group_by(country, ai_tool) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop")

p4b <- ggplot(country_tool, aes(x = ai_tool, y = reorder(country, mean_adoption), fill = mean_adoption)) +
    geom_tile(color = "white", linewidth = 0.8) +
    geom_text(aes(label = round(mean_adoption, 1)), fontface = "bold", size = 3.5) +
    scale_fill_gradient(low = "#fff9c4", high = "#e65100") +
    labs(title = "AI Tool Adoption Heatmap: Country × Tool",
         x = "AI Tool", y = NULL, fill = "Mean\nAdoption (%)") +
    theme_minimal(base_size = 13)

p4a | p4b
ggsave("country_analysis.png", width = 14, height = 12, dpi = 120)

country_size <- df %>%
    group_by(country, company_size) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop")

p4c <- ggplot(country_size, aes(x = company_size, y = mean_adoption, fill = company_size)) +
    geom_bar(stat = "identity", show.legend = FALSE) +
    facet_wrap(~country, nrow = 2) +
    scale_fill_brewer(palette = "Set2") +
    labs(title = "Adoption Rate by Company Size, Faceted by Country",
         x = "Company Size", y = "Mean Adoption Rate (%)") +
    theme_minimal(base_size = 11) +
    theme(axis.text.x = element_text(angle = 30, hjust = 1))

p4c
ggsave("country_size_facet.png", width = 14, height = 12, dpi = 120)


# ---- Year-over-year trends --------------------------------------------------
p5a <- df %>%
    group_by(year, company_size) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop") %>%
    ggplot(aes(x = year, y = mean_adoption, color = company_size, group = company_size)) +
    geom_line(linewidth = 1.2) + geom_point(size = 4) +
    scale_color_brewer(palette = "Set2") +
    labs(title = "YoY Adoption: Company Size",
         x = "Year", y = "Mean Adoption Rate (%)", color = "Company Size") +
    theme_minimal(base_size = 12)

p5b <- df %>%
    group_by(year, industry) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop") %>%
    ggplot(aes(x = year, y = mean_adoption, color = industry, group = industry)) +
    geom_line(linewidth = 1.2) + geom_point(size = 4) +
    scale_color_brewer(palette = "Dark2") +
    labs(title = "YoY Adoption: Industry",
         x = "Year", y = "Mean Adoption Rate (%)", color = "Industry") +
    theme_minimal(base_size = 12)

p5c <- df %>%
    group_by(year, age_group) %>%
    summarise(mean_adoption = mean(adoption_rate), .groups = "drop") %>%
    ggplot(aes(x = year, y = mean_adoption, color = age_group, group = age_group)) +
    geom_line(linewidth = 1.2) + geom_point(size = 4) +
    scale_color_brewer(palette = "Set1") +
    labs(title = "YoY Adoption: Age Group",
         x = "Year", y = "Mean Adoption Rate (%)", color = "Age Group") +
    theme_minimal(base_size = 12)

p5a | p5b | p5c
ggsave("yoy_trends.png", width = 16, height = 12, dpi = 120)


# ---- Summary table ----------------------------------------------------------
top_combos <- df %>%
  group_by(country, industry, company_size, age_group) %>%
  summarise(
    mean_adoption = round(mean(adoption_rate), 2),
    mean_dau      = round(mean(daily_active_users), 0),
    n             = n(),
    .groups = "drop"
  ) %>%
  arrange(desc(mean_adoption)) %>%
  head(20)

print(top_combos)
write_csv(top_combos, "top_adoption_combinations.csv")
