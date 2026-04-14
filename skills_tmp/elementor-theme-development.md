name: elementor-themes
description: Use when building Elementor-compatible themes, registering theme locations, creating dynamic tags, or extending the Finder. Covers register_location, theme_builder locations, elementor_theme_do_location, Theme_Document and theme conditions, Tag_Base for dynamic tags (register_tag, get_value, render), Finder extension (Category_Base, register via elementor/finder/register), Context_Menu customization (elements/context-menu/groups filter), Hello Elementor theme (elementor-hello-theme, hello_elementor_* filters), and hosting page cache integration hooks.

1. Theme Builder Locations
Registering Locations:
function theme_prefix_register_elementor_locations( $elementor_theme_manager ) {
    $elementor_theme_manager->register_all_core_location();
}
add_action( 'elementor/theme/register_locations', 'theme_prefix_register_elementor_locations' );

Register specific locations:
$elementor_theme_manager->register_location( 'header' );
$elementor_theme_manager->register_location( 'footer' );
$elementor_theme_manager->register_location( 'main-sidebar', [
    'label' => esc_html__( 'Main Sidebar', 'theme-name' ),
    'multiple' => true,
    'edit_in_content' => false,
] );

2. Theme Conditions
Extend \ElementorPro\Modules\ThemeBuilder\Conditions\Condition_Base.
Required methods: get_type(), get_name(), get_label(), check($args).

3. Dynamic Tags
Extend \Elementor\Core\DynamicTags\Tag.
Required methods: get_name(), get_title(), get_group(), get_categories(), render().

4. Finder
Extend \Elementor\Core\Common\Modules\Finder\Base_Category.
Methods: get_id(), get_title(), get_category_items().

5. Context Menu (JavaScript)
window.addEventListener( 'elementor/init', () => {
    elementor.hooks.addFilter( 'elements/context-menu/groups', ( customGroups, elementType ) => {
        // ... modifications
    } );
} );

6. Hello Elementor Theme Hooks
Filters: hello_elementor_post_type_support, hello_elementor_content_width, hello_elementor_page_title, etc.
