/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: 'class', // Enables dark mode based on a 'dark' class on an element
    content: [
      './templates/**/*.html', // Ensures all HTML files in templates folder are processed
      './static/**/*.js', // Processes JS files within static folder (if using Tailwind in JS)
      './**/templates/**/*.html', // Recursively handles HTML files in subfolders
    ],
    theme: {
      extend: {
        colors: {
          primary: '#FF6347', // Custom primary color (e.g., Tomato)
          secondary: '#4B0082', // Custom secondary color (e.g., Indigo)
        },
        fontSize: {
          xxs: '0.65rem', // Custom extra small font size
        },
        spacing: {
          128: '32rem', // Custom spacing size (used for padding, margin, etc.)
        },
      },
    },
    plugins: [
      require('@tailwindcss/typography'), // Adding Typography plugin for styled prose elements
    ],
  }
  