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
      gridTemplateColumns: {
        layout_mobile: "68px 1fr",
        layout: "300px 1fr",
      },
      width: {
        nav_mobile: "68px",
        nav: "600px",
      },
      maxWidth: {
        layout: "1265px",
        feed: "600px",
        widget: "350px",
      },
    },
  },
  plugins: [],
};
