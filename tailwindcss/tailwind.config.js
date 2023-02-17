/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: ["../views/*.html"],
  theme: {
    extend: {
      screens: {
        'sm': '500px',
        'md': '987px',
        'lg': '1265px',
      },
    },
    },
  plugins: [],
}
