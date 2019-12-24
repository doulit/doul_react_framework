import React,{useEffect} from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import TreeView from '@material-ui/lab/TreeView';
import TreeItem from '@material-ui/lab/TreeItem';
import Typography from '@material-ui/core/Typography';
import MailIcon from '@material-ui/icons/Mail';
import DeleteIcon from '@material-ui/icons/Delete';
import Label from '@material-ui/icons/Label';
import SupervisorAccountIcon from '@material-ui/icons/SupervisorAccount';
import InfoIcon from '@material-ui/icons/Info';
import ForumIcon from '@material-ui/icons/Forum';
import LocalOfferIcon from '@material-ui/icons/LocalOffer';
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';
import ArrowRightIcon from '@material-ui/icons/ArrowRight';
import * as service from '../settings/default';
import { Link } from '@material-ui/core';
let menu = []
const useTreeItemStyles = makeStyles(theme => ({
  root: {
    color: theme.palette.text.secondary,
    '&:focus > $content': {
      backgroundColor: `var(--tree-view-bg-color, ${theme.palette.grey[400]})`,
      color: 'var(--tree-view-color)',
    },
  },
  content: {
    color: theme.palette.text.secondary,
    borderTopRightRadius: theme.spacing(2),
    borderBottomRightRadius: theme.spacing(2),
    paddingRight: theme.spacing(1),
    fontWeight: theme.typography.fontWeightMedium,
    '$expanded > &': {
      fontWeight: theme.typography.fontWeightRegular,
    },
  },
  group: {
    marginLeft: 0,
    '& $content': {
      paddingLeft: theme.spacing(2),
    },
  },
  expanded: {},
  label: {
    fontWeight: 'inherit',
    color: 'inherit',
  },
  labelRoot: {
    display: 'flex',
    alignItems: 'center',
    padding: theme.spacing(0.5, 0),
  },
  labelIcon: {
    marginRight: theme.spacing(1),
  },
  labelText: {
    fontWeight: 'inherit',
    flexGrow: 1,
  },
}));

function StyledTreeItem(props) {
  const classes = useTreeItemStyles();
  const { labelText, labelIcon: LabelIcon, labelInfo, color, bgColor, ...other } = props;

  return (
    <TreeItem
      label={
        <div className={classes.labelRoot}>
          <LabelIcon color="inherit" className={classes.labelIcon} />
          <Typography variant="body2" className={classes.labelText}>
            {labelText}
          </Typography>
          <Typography variant="caption" color="inherit">
            {labelInfo}
          </Typography>
        </div>
      }
      style={{
        '--tree-view-color': color,
        '--tree-view-bg-color': bgColor,
      }}
      classes={{
        root: classes.root,
        content: classes.content,
        expanded: classes.expanded,
        group: classes.group,
        label: classes.label,
      }}
      {...other}
    />
  );
}

StyledTreeItem.propTypes = {
  bgColor: PropTypes.string,
  color: PropTypes.string,
  labelIcon: PropTypes.elementType.isRequired,
  labelInfo: PropTypes.string,
  labelText: PropTypes.string.isRequired,
};

const useStyles = makeStyles({
  root: {
    height: 264,
    flexGrow: 1,
    maxWidth: 400,
  },
});


const TreeViewCreate = (props) => {
  menuSearch();
  const classes = useStyles();
  return (    
    <TreeView
      className={classes.root}
      defaultExpanded={['3']}
      defaultCollapseIcon={<ArrowDropDownIcon />}
      defaultExpandIcon={<ArrowRightIcon />}
      defaultEndIcon={<div style={{ width: 24 }} />}
    >
    {getTreeItemsFromData(menu)}
    </TreeView>
  );
}

const handleClick = (id,link) => {
  console.log(id+"//"+link);
  if(id != undefined){
    // 메뉴클릭이벤트
    if(link == undefined || link == null){
      window.location.href = "#";    
    }else{
      window.location.href = link;    
    }
    

  }
}

const getTreeItemsFromData = treeItems => {
  return treeItems.map(treeItemData => {
    let children,color,bgColor = undefined;
    let labelIcon = Label;
    let clickEventId = treeItemData.id;
    if (treeItemData.subcategories && treeItemData.subcategories.length > 0) {
      children = getTreeItemsFromData(treeItemData.subcategories);
      labelIcon = LocalOfferIcon;
      clickEventId = undefined;
    }
    color = "#a250f5";
    bgColor = "#f3e8fd";

    return (
      <StyledTreeItem
        key={treeItemData.id}
        nodeId={String(treeItemData.id)}
        labelText={treeItemData.name}
        labelIcon={labelIcon}
        children={children}
        color={color}
        bgColor={bgColor}
        onClick={() => handleClick(clickEventId,treeItemData.link)}
        // onClick={() => setItems([...items, items.length])}
      />
    );
  });
};

function menuSearch() {
  service.search('/blog/category/sel/').then(res => {       
      menu = res.data;      
      console.log(menu)
      return res.data;
  });
}

export default function GmailTreeView() {
  const classes = useStyles();
  const [menuData, setMenuData] = React.useState();
  const callSearchApi = async() => {
    service.search('/blog/category/sel/').then(res => {       
        setMenuData( res.data );        
    });
    
  };
  useEffect(() => {
    callSearchApi();
  }, []);

  return (
    <TreeViewCreate 
        data={menuData}
    />
  );
}
