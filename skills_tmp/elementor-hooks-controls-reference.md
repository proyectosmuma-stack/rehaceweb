name: elementor-hooks
description: Use for hooking into Elementor's lifecycle, modifying existing widgets, or adjusting global editor settings. Covers elementor/widgets/register (widget loading), elementor/element/{widget_id}/{section_id}/before_section_end (adding controls to existing sections), elementor/editor/after_enqueue_scripts (JS/CSS in editor), elementor/frontend/after_enqueue_styles, elementor/document/save/data (processing layout data), and JS-side hooks (elementor.hooks.addFilter, elementor.settings.page.addChangeCallback).

1. Widget Registration
add_action( 'elementor/widgets/register', function( $widgets_manager ) {
    $widgets_manager->register( new \My_Custom_Widget() );
} );

2. Modifying Existing Widgets
Add control to existing section:
add_action( 'elementor/element/common/_section_style/before_section_end', function( $element, $args ) {
    $element->add_control( ... );
}, 10, 2 );

3. Editor Assets
add_action( 'elementor/editor/after_enqueue_scripts', function() {
    wp_enqueue_script( 'my-editor-js', ... );
} );

4. Frontend Assets
add_action( 'elementor/frontend/after_enqueue_styles', function() {
    wp_enqueue_style( 'my-frontend-css', ... );
} );

5. Data Formatting (PHP)
Filter 'elementor/frontend/builder_content_data' to manipulate the JSON structure before rendering.

6. Editor Hooks (JavaScript)
elementor.hooks.addAction( 'panel/open_editor/widget/button', function( panel, model, view ) {
    // Logic when button editor opens
} );

elementor.hooks.addFilter( 'editor/style/color-picker-palettes', function( currentPalettes ) {
    return [ '#ff0000', '#00ff00', '#0000ff' ];
} );

7. Dynamic Capability
Filter 'elementor/dynamic_tags/register' to add custom dynamic tag groups and tags.
