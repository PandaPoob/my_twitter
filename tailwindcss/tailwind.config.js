/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../views/*.html"],
  theme: {
    extend: {
      screens: {
        sm: "500px",
        md: "987px",
        lg: "1265px",
        xl: "1500px",
        xxl: "1800px",
      },
      maxWidth: {
        layout: "1800px",
        feed: "600px",
        widget: "350px",
      },
    },
  },
  plugins: [],
};
