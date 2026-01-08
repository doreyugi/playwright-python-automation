# Test Case 8: Verify All Products and product detail page
def test_all_products_and_product_detail(homepage):
    # 4. Click on 'Products' button
    all_product_page = homepage.header.click_products_button()
    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    all_product_page.is_all_products_page()
    # 6. The products list is visible
    all_product_page.product_list.is_product_list_visible()
    # 7. Click on 'View Product' of first product
    product_detail_page = all_product_page.product_list.click_view_nth_product(0)
    # 8. User is landed to product detail page
    # 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
    product_detail_page.is_product_detail_visible()

# Test Case 9: Search Product
def test_search_product(homepage):
    # 4. Click on 'Products' button
    all_product_page = homepage.header.click_products_button()
    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    all_product_page.is_all_products_page()
    # 6. Enter product name in search input and click search button
    keyword = "Top"
    all_product_page.search_product(keyword)
    # 7. Verify 'SEARCHED PRODUCTS' is visible
    all_product_page.is_searched_product_visible()
    # 8. Verify all the products related to search are visible
    all_product_page.product_list.is_product_list_visible()

