export default {
  beforeMount(el, { value }) {
    M.Tooltip.init(el, { html: value, position: "bot" });
  },
  unmounted(el) {
    const tooltip = M.Tooltip.getInstance(el);

    if (tooltip && tooltip.destroy()) {
      tooltip.destroy();
    }
  },
};
